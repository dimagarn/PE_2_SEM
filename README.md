[![flake8 Lint](https://github.com/dimagarn/PE_2_SEM/actions/workflows/flake8-lint.yml/badge.svg)](https://github.com/dimagarn/PE_2_SEM/actions/workflows/flake8-lint.yml)
[![pytest](https://github.com/dimagarn/PE_2_SEM/actions/workflows/pytest-tests.yml/badge.svg)](https://github.com/dimagarn/PE_2_SEM/actions/workflows/pytest-tests.yml)
# UrFU_SE_Final
Итоговый проект по предмету "Программная инженерия" (весенний семестр, 2024г)
## Участники команды
- Гарнышев Дмитрий Александрович, РИМ-130907;
- Кривошлык Александр Валерьевич, РИМ-130906;
- Репьева Марина Владимировна, РИМ-130906.
## Описание модели
[Модель](https://huggingface.co/facebook/bart-large-mnli) для zero-shot классификации текста на английском языке. Данная модель основана на [BART (large-sized model)](https://huggingface.co/facebook/bart-large) от компании facebook, обученной на датасете [MultiNLI (MNLI)](https://huggingface.co/datasets/nyu-mll/multi_nli) 
(подробнее ознакомиться с моделью можно по [ссылке](https://huggingface.co/facebook/bart-large-mnli)). В качестве входных данных принимается текст в виде строки; список меток (лейблов), на принадлежность к которым проверяется текст. В качестве выходных данных выводится словарь вида:  
```
{'labels': список меток,
 'scores': список вероятностей меток,
 'sequence': текст в виде строки, проверка которого осуществлялась}
```
Пример входных данных:
```
sequence_to_classify = "one day I will see the world"
candidate_labels = ['travel', 'cooking', 'dancing']
```
Пример выходных данных:  
```
{'labels': ['travel', 'dancing', 'cooking'],
 'scores': [0.9938651323318481, 0.0032737774308770895, 0.002861034357920289],
 'sequence': 'one day I will see the world'}
```
## Применение
Модель может пригодиться для классификации вопросов иностранных студентов по категориям FAQ.
## Использование модели
```python
from transformers import pipeline


classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")

sequence_to_classify = "one day I will see the world"
candidate_labels = ['travel', 'cooking', 'dancing']

classifier(sequence_to_classify, candidate_labels)

#{'labels': ['travel', 'dancing', 'cooking'],
# 'scores': [0.9938651323318481, 0.0032737774308770895, 0.002861034357920289],
# 'sequence': 'one day I will see the world'}
```
## Архитектура файлов проекта
```
PE_2_SEM/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── text_classifier.py
│
├── data/
│   └── data.json
│
├── tests/
│   ├── __init__.py
│   └── test_main.py
│
├── requirements.txt
└── README.md
```
## API
Данный API позволяет классифицировать текст на английском языке по категориям FAQ и получить ответ на типовой вопрос. Используются библиотеки:
- fastapi
- uvicorn
- transformers[torch]
- pydantic
- torch

Для запуска сервера необходимо в каталоге с файлами проекта ввести в консоли следующую команду:
```
uvicorn app.main:app
```  
После запуска сервера можно посылать POST-запросы к модели по локальному адресу [http://127.0.0.1:8000/predict/](http://127.0.0.1:8000/predict/) с помощью командной строки (терминала), POSTMAN или через интерфейс документации FastAPI:
![image](https://github.com/themrinch/PE_final_check/assets/136446022/be0e966a-9a76-42e3-9d38-87f7e93ae6e5)
![image](https://github.com/themrinch/PE_final_check/assets/136446022/7c83e133-6faa-4bfa-81e4-432555a972d3)
![image](https://github.com/themrinch/PE_final_check/assets/136446022/7f122453-5d35-4ef1-8f7e-003b4bd90fb0)
![image](https://github.com/themrinch/PE_final_check/assets/136446022/123f4e6a-ca17-4db8-8100-a0bc62ba9497)
## Тестирование
Реализованы тесты, проверяющие корректность работы API. Используются библиотеки:
- pytest
- fastapi
- httpx
- uvicorn
- transformers[torch]
- pydantic
- torch

Для запуска тестирования необходимо в каталоге с файлами проекта ввести в консоли следующую команду:
```
pytest
```
Далее достаточно дождаться окончания выполнения тестирования и узнать об успешности прохождения тестов:
```
============================== 4 passed in 20.25s ==============================
```
В данном репозитории также настроена система Continuous Integration: при выполнении push и pull_request в ветку 'main' в репозиторий GitHub выполняется автоматический запуск тестов.
