   function dateStart()
   {
       //月份对应天数
       MonHead = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

       //给年下拉框赋内容
       var y  = new Date().getFullYear();
       for (var i = (y-50); i < (y+50); i++) //以今年为准，前50年，后50年
           document.date.year.options.add(new Option(" "+ i +" 年", i));

       //给月下拉框赋内容
       for (var i = 1; i < 13; i++)
           document.date.month.options.add(new Option(" " + i + " 月", i));

       document.date.year.value = y;
       document.date.month.value = new Date().getMonth() + 1;
       var n = MonHead[new Date().getMonth()];
       if (  new Date().getMonth() ==1 && IsPinYear(yearvalue)  )
           n++;
       writeDay(n); //赋日期下拉框
       document.date.day.value = new Date().getDate();
   }

   if(document.attachEvent)
       window.attachEvent("onload", dateStart);
   else
       window.addEventListener('load', dateStart, false);

   function selectYear(str) //年发生变化时日期发生变化(主要是判断闰平年)
   {
       var monthvalue = document.date.month.options[document.date.month.selectedIndex].value;
       if (monthvalue == "")
       {
           var e = document.date.day;
           optionsClear(e);
           return;
       }
       var n = MonHead[monthvalue - 1];
       if (  monthvalue ==2 && IsPinYear(str)  )
           n++;
       writeDay(n);
   }

   function selectMonth(str)   //月发生变化时日期联动
   {
        var yearvalue = document.date.year.options[document.date.year.selectedIndex].value;
        if (yearvalue == "")
        {
            var e = document.date.day;
            optionsClear(e);
            return;
        }
        var n = MonHead[str - 1];
        if (  str ==2 && IsPinYear(yearvalue)  )
            n++;
            writeDay(n);
        }

   function writeDay(n)   //据条件写日期的下拉框
   {
       var e = document.date.day; optionsClear(e);
       for (var i=1; i<(n+1); i++)
           e.options.add(new Option(" "+ i + " 日", i));
   }

   function IsPinYear(year)//判断是否闰平年
   {
       return(  0 == year%4 && ( year%100 !=0 || year%400 == 0 )  );
   }

   function optionsClear(e)
   {
       e.options.length = 1;
   }