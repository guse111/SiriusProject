from transformers import MBartForConditionalGeneration, MBartTokenizer

# 1. Инициализируем токенизатор и модель.
# Токенизатор разбивает текст на токены, которые модель сможет "понять". Мы используем версию mBART, которая обучена на русскоязычных данных.
model_name = "facebook/mbart-large-50-many-to-many-mmt"
tokenizer = MBartTokenizer.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)

# 2. Пример текста без знаков препинания.
input_text = "привет. как дела?"
# 3. Токенизация текста.
# Токенизатор разбивает текст на токены и возвращает их в виде индексов, которые использует модель.
inputs = tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True)

# 4. Генерация пересказа.
# Модель генерирует текст на основе входных данных.
summary_ids = model.generate(inputs["input_ids"], max_length=100, num_beams=5, early_stopping=True)

# 5. Декодирование выхода.
# Раскодируем токены обратно в текст.
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print("Пересказ:", summary)

