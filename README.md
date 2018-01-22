# alertByTelegram

this is a simple example of HOWTO alert user.

alertByTelegram is a simple repeater who listen on mqtt channel `local/alert` for `message.type: user_alert`. It get the message, format with a human sense and send over telegram.

All you need is a bot token and a chatid, default values (as example, they don't work) are stored
on `mongodb/sfera/config/alert_by_telegram`

*If you stop the bot in your telegram chats you must reobtain a new chatid!*
