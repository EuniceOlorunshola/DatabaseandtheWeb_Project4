for $emp in json-doc ("company.json").employees[],
  $dept in json-doc ("company.json").departments[]
  where $dept.dname eq "Research" and $emp.worksFor eq $dept.dno return
  {
 "fname": $emp.fname,
 "minit": $emp.minit,
 "lname": $emp.lname,
 "address": $emp.address
}
