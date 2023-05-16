use moDB
db.orders.deleteMany({})

db.orders.insert({
  "ONO": 1020,
  "TAKENBY": 1000,
  "CUSTOMER": 1111,
  "RECEIVEDDATE": "1994-12-10",
  "SHIPPEDDATE": "1994-12-12",
  "ITEMS": [
     {
        "PARTNUMBER": 10506,
        "QUANTITY": 1
     },
     {
        "PARTNUMBER": 10507,
        "QUANTITY": 1
     },
     {
        "PARTNUMBER": 10508,
        "QUANTITY": 2
     },
     {
        "PARTNUMBER": 10509,
        "QUANTITY": 3
     }
  ]
})

db.orders.insert({
  "ONO": 1021,
  "TAKENBY": 1000,
  "CUSTOMER": 1111,
  "RECEIVEDDATE": "1995-01-12",
  "SHIPPEDDATE": "1995-01-15",
  "ITEMS": [
     {
        "PARTNUMBER": 10601,
        "QUANTITY": 4
     }
  ]
})

db.orders.insert({
  "ONO": 1022,
  "TAKENBY": 1001,
  "CUSTOMER": 2222,
  "RECEIVEDDATE": "1995-02-13",
  "SHIPPEDDATE": "1995-02-20",
  "ITEMS": [
     {
        "PARTNUMBER": 10601,
        "QUANTITY": 1
     },
     {
        "PARTNUMBER": 10701,
        "QUANTITY": 1
     }
  ]
})

db.orders.insert({
  "ONO": 1023,
  "TAKENBY": 1000,
  "CUSTOMER": 3333,
  "RECEIVEDDATE": "1997-06-20",
  "ITEMS": [
     {
        "PARTNUMBER": 10800,
        "QUANTITY": 1
     },
     {
        "PARTNUMBER": 10900,
        "QUANTITY": 1
     }
  ]
})

db.orders.insert({
  "ONO": 1025,
  "TAKENBY": 1002,
  "CUSTOMER": 3333,
  "RECEIVEDDATE": "1997-06-20",
  "ITEMS": [
     {
        "PARTNUMBER": 10800,
        "QUANTITY": 1
     },
     {
        "PARTNUMBER": 10900,
        "QUANTITY": 1
     }
  ]
})

db.orders.insert({
  "ONO": 1024,
  "TAKENBY": 1002,
  "CUSTOMER": 2222,
  "RECEIVEDDATE": "2014-12-10",
  "SHIPPEDDATE": "2014-12-12",
  "ITEMS": [
     {
        "PARTNUMBER": 10506,
        "QUANTITY": 1
     },
     {
        "PARTNUMBER": 10507,
        "QUANTITY": 1
     },
     {
        "PARTNUMBER": 10508,
        "QUANTITY": 2
     },
     {
        "PARTNUMBER": 10509,
        "QUANTITY": 3
     },
     {
        "PARTNUMBER": 10701,
        "QUANTITY": 3
     },
     {
        "PARTNUMBER": 10800,
        "QUANTITY": 3
     }
  ]
})
