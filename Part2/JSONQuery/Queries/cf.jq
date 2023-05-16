for $emp in json-doc("company.json").employees[]
where some $pro in json-doc("company.json").projects[] satisfies $pro.plocation eq "Houston" and $pro.pno eq $emp.worksFor
let $dept := json-doc("company.json").departments[$emp.dno - 1]
where not($dept.locations eq "Houston")
return
{
    "fname": $emp.fname,
    "minit": $emp.minit,
    "lname" : $emp.lname,
    "address" : $emp.address

}