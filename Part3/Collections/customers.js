use moDB
db.customers.deleteMany({})

db.customers.insert({
  "CNO": 1111,
  "CNAME": "Charles",
  "STREET": "123 Main St.",
  "CITY": "Wichita",
  "ZIP": 67226,
  "PHONE": "316-636-5555"
})

db.customers.insert({
  "CNO": 2222,
  "CNAME": "Bertram",
  "STREET": "237 Ash Avenue",
  "CITY": "Wichita",
  "ZIP": 67226,
  "PHONE": "316-689-5555"
})

db.customers.insert({
  "CNO": 3333,
  "CNAME": "Barbara",
  "STREET": "111 Inwood St.",
  "CITY": "Fort Dodge",
  "ZIP": 60606,
  "PHONE": "316-111-1234"
})
