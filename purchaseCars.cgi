#!c:\perl\bin\perl
# Bjorn Debooserie

use CGI qw ( :standard );
#print ( header() );
print "Content-type: text/html\n\n";

###DECODE######################################################
read(STDIN, $datastring, $ENV{"CONTENT_LENGTH"});		#step 1

@nameValuePairs = split (/&/, $datastring);				#step 2

foreach $pair (@nameValuePairs)
{
  ($name, $value) = split (/=/, $pair);					#step 3
	
  $name =~tr/+/ /;                                 		#step 4
  $name =~s/%([\da-fA-F]{2})/pack("C",hex($1))/eg; 		#step 4
  $value =~tr/+/ /;                                		#step 4
  $value =~s/%([\da-fA-F]{2})/pack("C",hex($1))/eg;		#step 4
  
	
  $formHash{$name} = $value;							#step 5
}
###DONE DECODE##################################################

###DATA SOURCE##################################################

$buttonInput = $formHash{"cc"}; 
$menuInputOne = $formHash{"expmonth"};
$menuInputTwo = $formHash{"expyear"};

%mailinglist = ("mailinglist" => "YES!");

###END OF DATA SOURCE##############################################

print <<PRINTBLOCK;
<html>
<head>
<title>$formHash{"name_first"}'s order</title>
</head>
<body style="background-color:#ffffcc;">
PRINTBLOCK

if ($ENV{"HTTP_COOKIE"} eq "")
	{
	print ( "<p style=\"text-align: center; color: red; font-size: 18pt; font-family: \'Times New Roman\';\">You big dummy! You didn't order anything yet!</p>" );
	print ( "<p style=\"text-align: center; color: red; font-size: 18pt; font-family: \'Times New Roman\';\">Why are you submitting an order without selecting anything to order??</p>" );
	print ( "<p style=\"text-align: center; color: red; font-size: 18pt; font-family: \'Times New Roman\';\">Please return to the website and order something!</p>" );
	print ( "<a style=\"margin: auto; color: blue; font-size: 18pt; font-family: \'Times New Roman\';\" href=\"../checkout.html\">Bjorn's Used Cars</a>" );
	last;
	}

print <<PRINTBLOCK;
<p style="color: red; font-size: 18pt; font-family: 'Times New Roman';">Thanks for your order, $formHash{"name_first"}.</p>
<table border="1">
	<tr>
		<td><p style="font-weight: bold; color: blue;">Name</p></td>
		<td><p>$formHash{"name_first"} $formHash{"name_last"}</p></td>
	</tr>
	<tr>
		<td><p style="font-weight: bold; color: blue;">Address</p></td>
		<td><p>$formHash{"address1"}</p></td>
	</tr>
	<tr>
		<td><p style="font-weight: bold; color: blue;">City</p></td>
		<td><p>$formHash{"city"}</p></td>
	</tr>
	<tr>
		<td><p style="font-weight: bold; color: blue;">State</p></td>
		<td><p>$formHash{"state"}</p></td>
	</tr>
	<tr>
		<td><p style="font-weight: bold; color: blue;">Zip</p></td>
		<td><p>$formHash{"zip"}</p></td>
	</tr>
PRINTBLOCK

print ( "<tr>" );
	print ( "<td colspan=\"2\" style=\"color: green; font-weight: bold;\">Credit Card Information</td>" );
print ( "</tr>" );
print ( "<tr>" );
	print ( "<td style=\"font-weight: bold; color: blue;\">Type</td>" );
	print ( "<td>$buttonInput</td>" );
print ( "</tr>" );

print <<PRINTBLOCK;
<tr>
	<td style=\"font-weight: bold; color: blue;\">Number</td>
	<td>$formHash{"ccnumber"}</td>
</tr>
PRINTBLOCK

print ( "<tr>" );
print ( "<td style=\"font-weight: bold; color: blue;\">Exp. Month</td>" );

if ($menuInputOne eq "1")
	{
	print ( "<td>January</td>" );
	}
if ($menuInputOne eq "2")
	{
	print ( "<td>February</td>" );
	}
if ($menuInputOne eq "3")
	{
	print ( "<td>March</td>" );
	}
if ($menuInputOne eq "4")
	{
	print ( "<td>April</td>" );
	}
if ($menuInputOne eq "5")
	{
	print ( "<td>May</td>" );
	}
if ($menuInputOne eq "6")
	{
	print ( "<td>June</td>" );
	}
if ($menuInputOne eq "7")
	{
	print ( "<td>July</td>" );
	}
if ($menuInputOne eq "8")
	{
	print ( "<td>August</td>" );
	}
if ($menuInputOne eq "9")
	{
	print ( "<td>September</td>" );
	}
if ($menuInputOne eq "10")
	{
	print ( "<td>October</td>" );
	}
if ($menuInputOne eq "11")
	{
	print ( "<td>November</td>" );
	}
if ($menuInputOne eq "12")
	{
	print ( "<td>December</td>" );
	}
	
print ( "</tr>" );
print ( "<tr>" );
	print ( "<td style=\"font-weight: bold; color: blue;\">Exp. Year</td>" );
	
if ($menuInputTwo eq "08")
	{
	print ( "<td>2008</td>" );
	}
if ($menuInputTwo eq "09")
	{
	print ( "<td>2009</td>" );
	}
if ($menuInputTwo eq "10")
	{
	print ( "<td>2010</td>" );
	}
if ($menuInputTwo eq "11")
	{
	print ( "<td>2011</td>" );
	}
if ($menuInputTwo eq "12")
	{
	print ( "<td>2012</td>" );
	}
if ($menuInputTwo eq "13")
	{
	print ( "<td>2013</td>" );
	}
	
print ( "</tr>" );	
print ( "</table>" );

print ( "<p style=\"color: teal; font-weight: bold; font-size: 16pt \">Do you wish to be added to our mailing list?" );

foreach $mailinglist1 (sort keys %mailinglist) #gets the keys of %purposes
	{
	if (exists $formHash{$mailinglist1})  #do the keys exist in $formHash?
		{
		print ( " $mailinglist{$mailinglist1} </p>" );  #print out the value assoc. w/each key
		}
	else 
		{
		print ( " No thanks. </p>" );
		}
	}
print ( "<p style=\"color: red; font-size: 18pt; font-family: \'Times New Roman\';\">Here are your purchases</p>" );


$allCookies = $ENV{"HTTP_COOKIE"};

#Split out the cookies
@cookie_array = split(';', $allCookies);

$len = @cookie_array;
$subtotal = 0;
print ( "<table border=\"1\">" );
print ( "<thead><th colspan=\"2\" style=\"color:blue; font-weight:bold;\">Items and Cost</th></thead><tbody>" );

for ($i = 0; $i < $len; $i++)
{
  @cookie_val = split("=", $cookie_array[$i]);
  print ( "<tr><td>$cookie_val[0]</td><td>\$$cookie_val[1]</td></tr>" );
  
  $subtotal = $subtotal + int($cookie_val[1]); 
}

if ($formHash{"state"} eq "AR")
	{
	$tax = 0.045;
	}
else
	{
	$tax = 0.055;
	}

$taxtotal = $subtotal * $tax;
$total = $subtotal + $taxtotal;

$subtotal = sprintf("%.2f", $subtotal);
$taxtotal = sprintf("%.2f", $taxtotal);
$total = sprintf("%.2f", $total);

print ( "<tr><td style=\"color:blue; font-weight:bold;\">Subtotal</td><td> \$$subtotal </td></tr>" ); 
print ( "<tr><td style=\"color:blue; font-weight:bold;\">Tax</td><td> \$$taxtotal </td></tr>" ); 
print ( "<tr><td style=\"color:blue; font-weight:bold;\">Grand Total</td><td> \$$total </td></tr>" ); 
print ( "</tbody></table>" );	
print ("</body></html>");

