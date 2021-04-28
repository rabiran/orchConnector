yikes = """{"entry":{"xmlns:d":"http://schemas.microsoft.com/ado/2007/08/dataservices","xmlns:m":"http://schemas.microsoft.com/ado/2007/08/dataservices/metadata","xmlns":"http://www.w3.org/2005/Atom","content":{"type":"application/xml","m:properties":{"d:RunbookId":{"type":"Edm.Guid","$t":"{runBookId}"},"d:Parameters":{"Data":{"Parameter":[{"ID":"SamAccountName","Value":"{SamAccountName}"},{"ID":"DisplayName","Value":"{DisplayName}"},{"ID":"GivenName","Value":"{GivenName}"},{"ID":"SurName","Value":"{SurName}"},{"ID":"Mail","Value":"{Mail}"},{"ID":"ExtensionAttribute1","Value":"{ExtensionAttribute1}"},{"ID":"ExtensionAttribute2","Value":"{ExtensionAttribute2}"},{"ID":"DistinguishedName","Value":"{DistinguishedName}"}]}}}}}}"""
yikes2 = """{"entry": {"@xmlns:d": "http://schemas.microsoft.com/ado/2007/08/dataservices", "@xmlns:m": "http://schemas.microsoft.com/ado/2007/08/dataservices/metadata", "@xmlns": "http://www.w3.org/2005/Atom", "content": {"@type": "application/xml", "m:properties": {"d:RunbookId": {"@type": "Edm.Guid", "#text": "{runBookId}"}, "d:Parameters": {"Data": {"Parameter": [{"ID": "SamAccountName", "Value": "{SamAccountName}"}, {"ID": "DisplayName", "Value": "{DisplayName}"}, {"ID": "GivenName", "Value": "{GivenName}"}, {"ID": "SurName", "Value": "{SurName}"}, {"ID": "Mail", "Value": "{Mail}"}, {"ID": "ExtensionAttribute1", "Value": "{ExtensionAttribute1}"}, {"ID": "ExtensionAttribute2", "Value": "{ExtensionAttribute2}"}, {"ID": "DistinguishedName", "Value": "{DistinguishedName}"}, {"ID": "DistinguishedName", "Value": "{DistinguishedName}"}]}}}}}}"""

xmlyikes = """<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<entry xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" 
xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" 
xmlns="http://www.w3.org/2005/Atom">
<content type="application/xml">
<m:properties>
<d:RunbookId type="Edm.Guid">{runBookId}</d:RunbookId>
<d:Parameters>
  <Data>
    <Parameter>
      <ID>SamAccountName</ID>
      <Value>{SamAccountName}</Value>
    </Parameter>
    <Parameter>
      <ID>DisplayName</ID>
      <Value>{DisplayName}</Value>
    </Parameter>
    <Parameter>
      <ID>GivenName</ID>
      <Value>{GivenName}</Value>
    </Parameter>
    <Parameter>
      <ID>SurName</ID>
      <Value>{SurName}</Value>
    </Parameter>
    <Parameter>
      <ID>Mail</ID>
      <Value>{Mail}</Value>
    </Parameter>
    <Parameter>
      <ID>ExtensionAttribute1</ID>
      <Value>{ExtensionAttribute1}</Value>
    </Parameter>
    <Parameter>
      <ID>ExtensionAttribute2</ID>
      <Value>{ExtensionAttribute2}</Value>
    </Parameter>
    <Parameter>
      <ID>DistinguishedName</ID>
      <Value>{DistinguishedName}</Value>
    </Parameter>
    <Parameter>
      <ID>DistinguishedName</ID>
      <Value>{DistinguishedName}</Value>
    </Parameter>
   </Data>
 </d:Parameters>
</m:properties>
</content>
</entry>"""
