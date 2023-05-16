use moDB
db.employees.deleteMany({})

db.employees.insert({
  "ENO": 1000,
  "ENAME": "Peter",
  "CITY": "Wichita",
  "ZIP": 67226,
  "HDATE": "1995-12-12"
})

db.employees.insert({
  "ENO": 1001,
  "ENAME": "Smith",
  "CITY": "Fort Dodge",
  "ZIP": 60606,
  "HDATE": "1992-01-01"
})

db.employees.insert({
  "ENO": 1002,
  "ENAME": "Brown",
  "CITY": "Kansas City",
  "ZIP": 50302,
  "HDATE": "1994-09-01"
})

db.employees.insert({
  "ENO": 1003,
  "ENAME": "John",
  "CITY": "St Louis",
  "ZIP": 64875,
  "HDATE": "1995-12-12"
})
