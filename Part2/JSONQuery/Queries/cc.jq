for $emp in json-doc ("company.json").employees[]
  where count($emp.dependents[]) >= 2
  return
  {
    "fname": $emp.fname,
    "minit": $emp.minit,
    "lname" : $emp.lname
  }