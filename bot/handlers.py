from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from services.system_info import SystemInfoServices
from services.network_info import NetworkInfoService
from services.screenshot import Screenshot
from services.power_manager import PowerManager

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Системная информация",callback_data='system_info')],
                [InlineKeyboardButton("Сетевая информация",callback_data='network_info')],
                [InlineKeyboardButton("Процессы",callback_data='processes')],
                [InlineKeyboardButton("Статус",callback_data='status')],
                [InlineKeyboardButton("Скриншот экрана",callback_data='screenshot')],
                [InlineKeyboardButton("Power Manager",callback_data='power_menu')]]
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
    elif query.data == 'screenshot':
        await send_screenshot(query)
    elif query.data == 'power_menu':
        await power_menu(query)
    elif query.data.startswith('power_'):
        await handle_power_command(query, query.data)

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


async def send_screenshot(query):
    try:
        await query.edit_message_text("📸 Делаю скриншот...")
        screenshot_data = Screenshot.take_screenshot()

        if screenshot_data is None:
            await query.edit_messgae_text("Не удалось")
            return
        system_info = SystemInfoServices.get_system_info()
        caption = f"📸 Скриншот системы\n🖥️ {system_info['system']['hostname']}\n⏰ {system_info['system']['uptime']}"
        await query.message.reply_photo(photo = screenshot_data, caption=caption)
    except Exception as e:
            await query.edit_message_text(f"❌ Ошибка при создании скриншота: {str(e)}")


async def power_menu(query):
    keyboard = [
        [InlineKeyboardButton("🔴 Выключить (30 сек)", callback_data='power_shutdown_30')],
        [InlineKeyboardButton("🔴 Выключить (1 мин)", callback_data='power_shutdown_60')],
        # [InlineKeyboardButton("🔄 Перезагрузить (1 мин)", callback_data='power_reboot_60')],
        [InlineKeyboardButton("💤 Гибернация", callback_data='power_hibernate')],
        [InlineKeyboardButton("⏹️ Отменить выключение", callback_data='power_cancel')],
        # [InlineKeyboardButton("📋 Информация", callback_data='power_info')],
        # [InlineKeyboardButton("🔙 Назад", callback_data='back_to_main')]

       
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "🔌 <b>Управление питанием компьютера</b>\n\n"
        "Выберите действие:",
        reply_markup=reply_markup,
        parse_mode='HTML'
    )


async def handle_power_command(query, command):
    try:

        result = None
        if command == 'power_shutdown_30':
            result = PowerManager.shutdown(30)
        elif command == 'power_shutdown_60':
            result = PowerManager.shutdown(60)
        # elif command == 'power_reboot_60':
        #     result = PowerManager.reboot(60)
        elif command == 'power_hibernate':
            result = PowerManager.hibernate()
        elif command == 'power_cancel':
            result = PowerManager.cancel_shutdown()
        # elif command == 'power_info':
        #     result = PowerManager.get_power_info()
        # elif command == 'back_to_main':
        #     await start_command(query, None)
        #     return
        
        if command != 'power_info':
            message = result['message'] if result['success'] else f"❌ {result['error']}"
            await query.edit_message_text(message)
        # else:
        #     # Показываем информацию о системе
        #     info = result
        #     message = "📋 <b>Информация о системе</b>\n\n"
        #     message += f"<b>Система:</b> {info['system']}\n"
        #     message += f"<b>Платформа:</b> {info['platform']}\n"
        #     message += f"<b>Поддерживаемые команды:</b> {', '.join(info['supported_commands'])}\n\n"
        #     message += "<b>Примеры команд:</b>\n"
        #     for cmd, example in info['example_commands'].items():
        #         message += f"  {cmd}: <code>{example}</code>\n"
            
        #     await query.edit_message_text(message, parse_mode='HTML')
            
    except Exception as e:
        await query.edit_message_text(f"❌ Ошибка: {str(e)}")

