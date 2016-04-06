// JavaScript Document
function get_term()
{
  var o=document.f.term
  return o.options[o.options.selectedIndex].text
}

function get_week()
{
  var w=document.f.week
  return parseInt(w.options[w.options.selectedIndex].value)
}

function term_change()
{
  var w=document.f.week
  var t=Terms[get_term()]
  w.options.length=t.length-1
  w.options.selectedIndex=0
  for(var i=1;i<t.length;i++)
  {
    w.options[i-1].value=i
    w.options[i-1].text=
      i+" ("+simplify_date(t[i][0])+"-"+simplify_date(t[i][1])+")"
  }
  week_change()
}

function simplify_date(d)
{
  return d.substr(5,2)+"/"+d.substr(8,2)
}

function week_change()
{
  var f=document.f
  f.curTerm.value=get_term()
  f.curWeek.value=get_week()
  document.f.submit()
}
