let $emp := json-doc("company.json").employees[]
let $dept := json-doc("company.json").departments[]
 let $dept := $emp.dependents
 where $dept.dependentName eq $emp.fname
 return {
   "fname": $emp.fname,
  "minit": $emp.minit,
  "lname": $emp.lname
 }
