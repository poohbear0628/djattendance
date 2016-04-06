// For teamStatistics
function checkInt(el)
{

if(!isInteger(el.value) && (el.value != ''))
{
alert('This is not an integer.');
el.value = "";
el.focus();
}
}

function isInteger (s)
   {
      var i;

      if (isEmpty(s))
      if (isInteger.arguments.length == 1) return 0;
      else return (isInteger.arguments[1] == true);

      for (i = 0; i < s.length; i++)
      {
         var c = s.charAt(i);

         if (!isDigit(c)) return false;
      }

      return true;
   }

   function isEmpty(s)
   {
      return ((s == null) || (s.length == 0))
   }

   function isDigit (c)
   {
      return ((c >= "0") && (c <= "9"))
   }


// Canonicalize any given roll status string.
function simplify_rollstr(s,warn)
{
  if(!InvalidRollStatusesRegex) //this is a pretty ugly fix to a problem that only shows up for internet explorer -Allen Webb
  {
    var AllRollStatuses="ATLU";
    var ValidRollStatusesRegex=new RegExp("["+AllRollStatuses+"]","g")
    var InvalidRollStatusesRegex=new RegExp("[^"+AllRollStatuses+"]","g")
  }

  try{
  if(s.length==0)return s
  var err=""
  
  // clean up whitespace, upper
  s=s.replace(/\s+/g,"").toUpperCase()
  
  // Check for invalid characters.
  var t=s
  s=s.replace(InvalidRollStatusesRegex,"")
  if(warn&&t!=s)
  {
    var un=t.replace(ValidRollStatusesRegex,"")
    alert("Unknown roll status"+(un.length==1?"":"es")+": "+un+"\n"
         +"Valid values are: "+AllRollStatuses)
  }
  
  // Remove all duplicates.
  if(s.length>1)
  {
    var t="",seen=[]
    for(var i=0;i<s.length;i++)
    {
      var c=s.charAt(i)
      if(seen[c])continue
      seen[c]=1
      t+=c
    }
    s=t
  }
  
  // Check for mutually-exclusive T and A.
  if(warn&&s.indexOf('T')!=-1 && s.indexOf('A')!=-1)
  {
    alert("Roll statuses `T' and `A' cannot exist together.\n"
         +"Removing both `T' and `A' ... ...")
    s=s.replace(/[TA]/g,"")
  }

  // Check for mutually-exclusive S.
  if(warn&&s.indexOf('S')!=-1)
  {
    alert("Roll statuses `S' cannot exist.\n"
         +"Removing `S' ... ...")
    s=s.replace(/[S]/g,"")
  } 
  
  // Check for mutually-exclusive P and anything.
  if(warn&&s.indexOf('P')!=-1 && s.length>1)
  {
    alert("Roll statuses `P' cannot exist together with any other designation.\n"
         +"Removing `P' ... ...")
    s=s.replace(/[P]/g,"")
  }
   
  // Sort.
  for(var i=s.length-1;i>=1;i--)
    for(var j=i-1;j>=0;j--)
      if(s.charCodeAt(i)<s.charCodeAt(j))
      {
        var c=s.charAt(i)
        s=s.substring(0,i)+s.charAt(j)+s.substring(i+1)
        s=s.substring(0,j)+c+s.substring(j+1)
      }

  if(warn&&err)alert(err)
  }catch(e){alert(e.message)}
  return s
}
// Check whether a certain roll value had changed or not.
function checkChange(o)
{
  o.value=simplify_rollstr(o.value,1)
  if(changed) {return}
  
  if(!/^check/.test(o.name)) {return}
  var s=o.name.substring(5)
  
  var origValue=eval("document.f.oldck"+s+".value")
  if(simplify_rollstr(origValue,0)!=o.value)setchanged()
}
function setchanged(){changed=1}

function click_submit_save(save,link)
{
  if(!changed){if(save)return;location.href=link;return}
  document.f.FormSubmit.value=save?'save':'submit'
  document.f.submit()
}
function click_submit(link){click_submit_save(0, link)}
function click_save(link){click_submit_save(1, link)}
function click_cancel(link)
{
  if(!changed||confirm("Are you sure you want to discard all changes?"))
    location.href=link;
}
