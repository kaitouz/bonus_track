# 1. Общие положения
## 1.1 Наименование НИР

Предсказание цены ноутбука по его описанию

## 1.2 Формулировка проблемы

Dự án nhằm giúp người dùng có thể dễ dàng xác định được giá của laptop dựa trên những miêu tả về thông số cấu hình của nó. Dự án nằm trong khuôn khổ đào tạo, không có mục đích kinh doanh. 

## 1.3 Нормативная документация

...

## 1.4 Источники разработки
- Nhân lực:
    + Được tạo ra bỏi đội ngũ Đã có kinh nghiệm triển khai mô hình machine learning quy mô nhỏ. 
- Tài nguyên:
    + Publicly available Python libraries for Telegram bot development (e.g., python-telegram-bot)
    + Open-source machine learning libraries (e.g., TensorFlow, scikit-learn)
    + Publicly available laptop price datasets (if applicable)


## 1.5 Консультанты со стороны Заказчика
....
## 1.6. Требования к патентной чистоте и лицензированию
....
# 2 Список терминов и определений

# 3 Список сокращений

# 4 Цели и задачи работы
- Mục tiêu:
    + Phát triển một Telegram-bot giúp người dùng có thể dễ dàng, nhanh chóng dự đoán được giá của laptop dựa trên mô tả.
- Tasks:
    + 1. Phân tích dự án: vấn đề, bài toán, yêu cầu, mục tiêu.
    + 2. Thu thập dữ liệu: từ các publicy laptop prices datasets, crawl dữ liệu từ các trang web bán hàng.
    + 3. Phân tích và chuẩn bị dữ liệu.
    + 4. Phát triển mô hình
    + 5. Phát triển ứng dụng telegram-bot và triển khai mô hình.
    + 6. Monitor, validate ứng dụng.

# 5 Позиционирование

Thực hiện MLOps level 0 - Các bước được thực hiện thủ công.


# 6 Входные и выходные данные

**Inputs:**
- User sends a Telegram message with a description of a laptop (including specifications like brand, model, CPU, RAM, storage etc.).
**Outputs:**
- Bot responds with a predicted price range for the described laptop. Optionally, the bot can provide additional information like confidence level in the prediction.

# 7 Функциональные требования

# 8 Ограничения

# 9 Допущения и зависимости

# 10 Системные требования и производительность

# 11. Атрибуты качества

# 12. Требования к защищенности

# 13. Требования к развертыванию

# 14. Документирование

# 15. Порядок приемки работ

# 16. Календарный план работ

# 17. Приложения