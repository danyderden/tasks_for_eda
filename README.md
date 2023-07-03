### Task 1

Instruction:
1. Create RandomCity object:
```python
object = RandomCity(route="<PATH_TO_JSON_FILE_WITH_CITIES_INFO>")
```
2. Call get_random_city():
```python
object.get_random_city()
```
Format of data in json file with cities info:
```json
[
  {
    "name": "Saint-Petersburg",
    "population": 900
  },
  {
    "name": "Moscow",
    "population": 2000
  },
  {
    "name": "Rostov",
    "population": 500
  }
]
```

____
### Task 2

Setup:
1. Install requirements: ``` pip install -r 'req.txt' ```
2. Create telegram bot. [Instruction](https://core.telegram.org/bots/features#botfather).
3. Create google sheet. [Instruction](https://support.google.com/docs/answer/49114?hl=en-GB&ref_topic=9055343&sjid=10807197133696226886-EU).
4. Get credentials json file. [Instruction](https://developers.google.com/workspace/guides/create-credentials?hl=en).
5. Create .env file in source directory and insert following variables:
   * TOKEN — token of telegram bot.
   * SHEET_ID — id of sheet for collecting message info. [Instruction](https://developers.google.com/sheets/api/guides/concepts#spreadsheet).
   * CREDENTIALS_FILE — path to json file with credentials.
6. Insert to A1 *login*, to B1 *text* and to C1 *time* to sheet.
