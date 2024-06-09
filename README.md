[![flake8 Lint](https://github.com/dimagarn/PE_2_SEM/actions/workflows/flake8-lint.yml/badge.svg)](https://github.com/dimagarn/PE_2_SEM/actions/workflows/flake8-lint.yml)
[![pytest](https://github.com/dimagarn/PE_2_SEM/actions/workflows/pytest-tests.yml/badge.svg)](https://github.com/dimagarn/PE_2_SEM/actions/workflows/pytest-tests.yml)
[![Docker Image CI](https://github.com/dimagarn/PE_2_SEM/actions/workflows/docker-image.yml/badge.svg)](https://github.com/dimagarn/PE_2_SEM/actions/workflows/docker-image.yml)
[![Docker Publish](https://github.com/dimagarn/PE_2_SEM/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/dimagarn/PE_2_SEM/actions/workflows/docker-publish.yml)
# UrFU_SE_Final & UrFU_MLOps_Final
Итоговые проекты по предметам "Программная инженерия" и "Автоматизация машинного обучения" (весенний семестр, 2024г)
## Участники команды (Программная инженерия)
- Гарнышев Дмитрий Александрович, РИМ-130907;
- Кривошлык Александр Валерьевич, РИМ-130906;
- Репьева Марина Владимировна, РИМ-130906.
## Участники команды (Автоматизация машинного обучения)
- Гарнышев Дмитрий Александрович, РИМ-130907;
- Репьева Марина Владимировна, РИМ-130906;
- Юрин Михаил Евгеньевич, РИМ-130907.
## Конвеер API приложения (итоговый проект по предмету "Автоматизация машинного обучения")
В процессе выполнения итогового проекта по предмету "Автоматизация машинного обучения" были выполнены следующие виды работ:
- добавлены тесты на проверку работы модели при классификации данных, оценка работы модели проводилась с помощью метрики accuracy от scikit-learn;
- настроены версионирование данных с помощью dvc и синхронизация данных с удаленным хранилищем;
- API приложение реализовано в виде образа docker, сборка которого проводится в конвеере jenkins;
- настроена оркестрация приложения с помощью ci/cd (jenkins).

Кроме того, в репозитории была настроена система Continuous Integration: при выполнении push и pull_request в ветку 'main' в репозиторий GitHub выполняется автоматическая сборка образа docker и его размещение в программных пакетах.
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
├── Dockerfile
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
![image](https://github.com/dimagarn/PE_2_SEM/assets/136446022/0cfbba3b-f115-428e-a726-e483f7ba3511)
![image](https://github.com/dimagarn/PE_2_SEM/assets/136446022/aa74b24a-75b9-4ba4-a4f6-7915d076ef44)
![image](https://github.com/dimagarn/PE_2_SEM/assets/136446022/58355c60-9c5d-482b-bf60-f89e2a11ece3)
![image](https://github.com/dimagarn/PE_2_SEM/assets/136446022/b3034c24-ed46-4ea4-af28-d574e1aff731)
![image](https://github.com/dimagarn/PE_2_SEM/assets/136446022/04e1112b-48ff-4efb-88cd-92471b6da0f8)
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
