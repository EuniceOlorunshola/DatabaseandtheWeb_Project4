let $dept := (
  for $p in json-doc ("company.json").projects[]
  where $p.dno eq 5
  return $p.pnumber
)
for $emp in json-doc("company.json").employees[]
let $emp_proj := distinct-values(for $w in $emp.worksFor
return $w.pno
)
where count(distinct-values($dept)) eq count(distinct-values($emp_proj))
  return {
    "fname": $emp.fname,
   "minit": $emp.minit,
   "lname": $emp.lname
 }
