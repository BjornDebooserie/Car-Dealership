#!c:\perl\bin\perl
# Bjorn Debooserie

use CGI qw ( :standard );
print ( header() );

###DECODE######################################################
$queryString = $ENV{"QUERY_STRING"};					#step 1

@nameValuePairs = split (/&/, $queryString);			#step 2

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

print <<PRINTBLOCK;
<html>
<head>
<title>Thanks for ordering, $formHash{"name_first"}</title>
</head>
<body style="background-color:#ffffcc;">
<p style="color: red; font-size: 18pt; font-family: 'Times New Roman';">Thanks for your order, $formHash{"name_first"}.</p>
<table border="1">
	<tr>
		<td><p style="font-weight: bold; color: blue;">Name:</p></td>
		<td><p>$formHash{"name_first"} $formHash{"name_last"}</p></td>
	</tr>
	<tr>
		<td><p style="font-weight: bold; color: blue;">Address:</p></td>
		<td><p>$formHash{"address1"}</p></td>
	</tr>
	<tr>
		<td><p style="font-weight: bold; color: blue;">City:</p></td>
		<td><p>$formHash{"city"}</p></td>
	</tr>
	<tr>
		<td><p style="font-weight: bold; color: blue;">State:</p></td>
		<td><p>$formHash{"state"}</p></td>
	</tr>
	<tr>
		<td><p style="font-weight: bold; color: blue;">Zip:</p></td>
		<td><p>$formHash{"zip"}</p></td>
	</tr>
</table>
<p style="color: red; font-size: 18pt; font-family: 'Times New Roman';">Here are your purchases</p>
PRINTBLOCK

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

