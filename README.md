# PrintBot

Welcome to PrintBot, a Telegram bot designed to provide the following services:
- Monitor and check messages in groups
- Facilitate the creation of online orders

## Commands

The bot supports a variety of commands for users and admins.

### User Commands

- `/start`: Комманда запуска бота
- `/help`: Справка по использованию бота
- `/faq`: Частые вопросы
- `/online_order`: Сделать онлайн заказ
- `/payment_methods`: Способы оплаты

### Admin Commands

- `/change_settings`: Изменение настроек
analyze chat content. If a chat contains a "PrintMessage", the bot sends a message notification to the admin.

## Setup

```
git clone git@github.com:AntonZimyanin/printBot.git
```

```
cd printBot
```

```
docker build -t bot .
```

```
docker run -it --rm --name bot    
```