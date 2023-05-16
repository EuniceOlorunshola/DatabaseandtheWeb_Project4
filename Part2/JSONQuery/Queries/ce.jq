for $emp in json-doc("company.json").employees
let $supe := $emp.supervisor
where $supe.fname eq "Franklin" and $supe.lname eq "Wong"
 return {
   "fname": $emp.fname,
  "minit": $emp.minit,
  "lname": $emp.lname
 }