from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from services.system_info import SystemInfoServices
from services.network_info import NetworkInfoService

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Системная информация",callback_data='system_info')],
                [InlineKeyboardButton("Сетевая информация",callback_data='network_info')],
                [InlineKeyboardButton("Процессы",callback_data='processes')],
                [InlineKeyboardButton("Статус",callback_data='status')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Pick option",reply_markup=reply_markup)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'system_info':
        await send_system_info(query)
    elif query.data == 'network_info':
        await send_network_info(query)
    elif query.data == 'processes':
        await send_processes_info(query)
    elif query.data == 'status':
        await send_status_info(query)


async def send_system_info(query):
    system_info = SystemInfoServices.get_system_info()

    if 'error' in system_info:
        await query.edit_message_text(system_info['error'])
        return
    
    message = "🖥️ <b>Системная информация</b>\n\n"
    message += f"<b>Система:</b>\n"
    message += f"  ОС: {system_info['system']['os']}\n"
    message += f"  Хост: {system_info['system']['hostname']}\n"
    message += f"  Архитектура: {system_info['system']['architecture']}\n"
    message += f"  Время работы: {system_info['system']['uptime']}\n\n"
    
    message += f"<b>Процессор:</b>\n"
    message += f"  Использование: {system_info['cpu']['usage']}\n"
    message += f"  Ядра: {system_info['cpu']['cores']}\n"
    message += f"  Частота: {system_info['cpu']['frequency']}\n\n"
    
    message += f"<b>Память:</b>\n"
    message += f"  Использование: {system_info['memory']['usage']}\n"
    message += f"  Всего: {system_info['memory']['total']}\n"
    message += f"  Использовано: {system_info['memory']['used']}\n"
    message += f"  Доступно: {system_info['memory']['available']}\n\n"
    
    message += f"<b>Диск:</b>\n"
    message += f"  Использование: {system_info['disk']['usage']}\n"
    message += f"  Всего: {system_info['disk']['total']}\n"
    message += f"  Использовано: {system_info['disk']['used']}\n"
    message += f"  Свободно: {system_info['disk']['free']}"

    await query.edit_message_text(message, parse_mode='HTML')

async def send_processes_info(query):
    processes = SystemInfoServices.get_run_processess(limit=15)

    message = "📊 <b>Топ процессов по CPU</b>\n\n"

    if isinstance(processes,str):
        message+=processes
    else:
        for i,proc in enumerate(processes,1):
            name = proc['name'][:20] + '...' if len(proc['name']) > 20 else proc['name']
            cpu = proc['cpu_percent'] or 0
            memory = proc['memory_percent'] or 0
            message += f"{i:2d}. {name:<23} CPU: {cpu:5.1f}% MEM: {memory:4.1f}%\n"
    
    await query.edit_message_text(message,parse_mode = 'HTML')

async def send_network_info(query):
    network_info = NetworkInfoService.get_net_info()

    if 'error' in network_info:
        await query.edit_message_text(network_info['error'])
        return
    
    message = "🌐 <b>Сетевая информация</b>\n\n"
    message += f"<b>Основное:</b>\n"
    message += f"  Хостнейм: {network_info['hostname']}\n"
    message += f"  Локальный IP: {network_info['local_ip']}\n"
    message += f"  Внешний IP: {network_info['external_ip']}\n\n"
    
    message += f"<b>Статистика сети:</b>\n"
    message += f"  Отправлено: {network_info['network_stats']['bytes_sent']}\n"
    message += f"  Получено: {network_info['network_stats']['bytes_recv']}\n"
    message += f"  Пакеты отправлено: {network_info['network_stats']['packets_sent']}\n"
    message += f"  Пакеты получено: {network_info['network_stats']['packets_recv']}\n\n"
    
    message += f"<b>Сетевые интерфейсы:</b>\n"

    for interface, addresses in network_info['interfaces'].items():
        if addresses:
            message += f"  {interface}:\n"
            for adr in addresses:
                message += f"    IP: {adr['address']}\n"
    
    await query.edit_message_text(message, parse_mode = 'HTML')


async def send_status_info(query):
    system_info = SystemInfoServices.get_system_info()
    if 'error' in system_info:
        await query.edit_message_text(system_info['error'])
        return
    
    cpu_usage = float(system_info['cpu']['usage'].replace('%',''))
    memory_usage = float(system_info['memory']['usage'].replace('%',''))
    disk_usage = float(system_info['disk']['usage'].replace('%',''))

    def get_status_emoji(usage):

        if usage < 70:
            return "🟢"
        elif usage < 90:
            return "🟡"
        else:
            return "🔴"
        
    
    message = "📈 <b>Статус системы</b>\n\n"
    message += f"{get_status_emoji(cpu_usage)} <b>CPU:</b> {system_info['cpu']['usage']}\n"
    message += f"{get_status_emoji(memory_usage)} <b>Память:</b> {system_info['memory']['usage']}\n"
    message += f"{get_status_emoji(disk_usage)} <b>Диск:</b> {system_info['disk']['usage']}\n\n"
    message += f"<b>Время работы:</b> {system_info['system']['uptime']}"
    
    await query.edit_message_text(message, parse_mode='HTML')