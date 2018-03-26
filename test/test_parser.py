import unittest

from babynames.parser import Parser


class TestParser(unittest.TestCase):

    def test_get_male_name_count(self):
        parser = Parser(DATA)
        data = parser.get_male_counts()
        expected = {
            "Noah":    19144,
            "Liam":    18342,
            "Mason":   17092,
            "Jacob":   16712,
            "William": 16687,
            "Ethan":   15619,
            "Michael": 15323,
            "Alexander":   15293,
            "James":   14301,
            "Daniel":  13829,
            "Elijah":  13694,
            "Benjamin":    13687,
            "Logan":   13579,
            "Aiden":   13296,
            "Jayden":  12878,
            "Matthew": 12809,
            "Jackson": 12121,
            "David":   12078,
            "Lucas":   12078,
            "Joseph":  11995
        }
        self.assertEqual(expected, data)
        
        

DATA = """
<head><title>Popular Baby Names</title>
<meta name="dc.language" scheme="ISO639-2" content="eng">
<meta name="dc.creator" content="OACT">
<meta name="lead_content_manager" content="sckunkel">
<meta name="coder" content="jlkunkel">
<meta name="dc.date.reviewed" scheme="ISO8601" content="2015-02-12">
<!-- Input: year=2014, top=20, number=n -->
</head>
<body bgcolor="#ffffff" text="#000000" topmargin="1" leftmargin="0">
<table width="100%" border="0" cellspacing="0" cellpadding="1">
<tbody>
  <tr valign="middle"> 
   <td align="left" width="25%">
        <a href="http://www.ssa.gov"><img src="../OACT/templateimages/ssalogo.png" border="0"></a></td>
   <th><h1>Popular Names in 2014</h1></th>
  </tr>
  <tr bgcolor="#333366"><td colspan="2" height="1"></td></tr>
</tbody></table>
<script type="text/javascript" src="../OACT/babynames/chkinput.js"></script>
<table width="100%" border="0" cellspacing="0" cellpadding="4" summary="formatting">
  <tr valign="top"> 
    <td width="25%" bgcolor="#eeeeee">
        <a href="../OACT/babynames/index.html">Popular baby names</a><p>
      <a href="../OACT/babynames/background.html">Background information</a>
      <p><br />
      &nbsp; Select another <label for="yob">year of birth</label>?<br />      
      <form name="popnames" method="post" action="/cgi-bin/popularnames.cgi"
       onSubmit="return submitIt();">
      &nbsp; <input type="text" name="year" id="yob" size="4" value="2014">
      <input type="hidden" name="top" value="20">
      <input type="hidden" name="number" value="n">
      &nbsp; <input type="submit" value="   Go  "></form>
    </td>
    <td>
<p align="center">
<table width="72%" border="1" bordercolor="#aaaabb"
 cellpadding="2" cellspacing="0" summary="Popularity for top 20"><caption><b>Popularity in 2014</b></caption>
<tr align="center" valign="bottom">
  <th scope="col" width="12%" bgcolor="#eeeeee">Rank</th>
  <th scope="col" width="22%" bgcolor="#99ccff">Male name</th>
<th scope="col" width="22%" bgcolor="#99ccff">Number of<br /> males</th>
<th scope="col" width="22%" bgcolor="pink">Female name</th>
<th scope="col" width="22%" bgcolor="pink">Number of<br /> females</th></tr>
<tr align="right">
 <td>1</td> <td>Noah</td><td>19,144</td>
 <td>Emma</td>
<td>20,799</td>
</tr>
<tr align="right">
 <td>2</td> <td>Liam</td><td>18,342</td>
 <td>Olivia</td>
<td>19,674</td>
</tr>
<tr align="right">
 <td>3</td> <td>Mason</td><td>17,092</td>
 <td>Sophia</td>
<td>18,490</td>
</tr>
<tr align="right">
 <td>4</td> <td>Jacob</td><td>16,712</td>
 <td>Isabella</td>
<td>16,950</td>
</tr>
<tr align="right">
 <td>5</td> <td>William</td><td>16,687</td>
 <td>Ava</td>
<td>15,586</td>
</tr>
<tr align="right">
 <td>6</td> <td>Ethan</td><td>15,619</td>
 <td>Mia</td>
<td>13,442</td>
</tr>
<tr align="right">
 <td>7</td> <td>Michael</td><td>15,323</td>
 <td>Emily</td>
<td>12,562</td>
</tr>
<tr align="right">
 <td>8</td> <td>Alexander</td><td>15,293</td>
 <td>Abigail</td>
<td>11,985</td>
</tr>
<tr align="right">
 <td>9</td> <td>James</td><td>14,301</td>
 <td>Madison</td>
<td>10,247</td>
</tr>
<tr align="right">
 <td>10</td> <td>Daniel</td><td>13,829</td>
 <td>Charlotte</td>
<td>10,048</td>
</tr>
<tr align="right">
 <td>11</td> <td>Elijah</td><td>13,694</td>
 <td>Harper</td>
<td>9,564</td>
</tr>
<tr align="right">
 <td>12</td> <td>Benjamin</td><td>13,687</td>
 <td>Sofia</td>
<td>9,542</td>
</tr>
<tr align="right">
 <td>13</td> <td>Logan</td><td>13,579</td>
 <td>Avery</td>
<td>9,517</td>
</tr>
<tr align="right">
 <td>14</td> <td>Aiden</td><td>13,296</td>
 <td>Elizabeth</td>
<td>9,492</td>
</tr>
<tr align="right">
 <td>15</td> <td>Jayden</td><td>12,878</td>
 <td>Amelia</td>
<td>8,727</td>
</tr>
<tr align="right">
 <td>16</td> <td>Matthew</td><td>12,809</td>
 <td>Evelyn</td>
<td>8,692</td>
</tr>
<tr align="right">
 <td>17</td> <td>Jackson</td><td>12,121</td>
 <td>Ella</td>
<td>8,489</td>
</tr>
<tr align="right">
 <td>18</td> <td>David</td><td>12,078</td>
 <td>Chloe</td>
<td>8,469</td>
</tr>
<tr align="right">
 <td>19</td> <td>Lucas</td><td>12,078</td>
 <td>Victoria</td>
<td>7,955</td>
</tr>
<tr align="right">
 <td>20</td> <td>Joseph</td><td>11,995</td>
 <td>Aubrey</td>
<td>7,589</td>
</tr>
<tr><td colspan="5"><small>Note: Rank 1 is the most popular,
rank 2 is the next most popular, and so forth. <p>All names are from Social Security card applications
              for births that occurred in the United States.
</table></p>
</td></tr></table>
<table width="100%" border="0" cellpadding="1" cellspacing="0">
  <tr bgcolor="#333366"><td height="1" colspan="2"></td></tr>
  <tr>
    <td width="26%" valign="middle">&nbsp;</td>
    <td valign="top"><small>
       <a href="http://www.ssa.gov/privacy.html">Privacy Policy</a>&nbsp;
     | <a href="http://www.ssa.gov/websitepolicies.htm">Website Policies
        &amp; Other Important Information</a>&nbsp;
     | <a href="http://www.ssa.gov/sitemap.htm">Site Map</a></small></td>
  </tr>
</table>
</body></html>
"""
