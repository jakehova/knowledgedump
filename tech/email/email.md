# Email

**SPF (Sender Policy Framework)**
* Purpose: Prevents domain spoofing 
* Works by comparing sender actual IP address to the list of IP addresses authorized to send email from that domain.
  * The IP list is published in the domain's DNS record.
* [Standard](https://tools.ietf.org/html/rfc7208) and [Updated](https://tools.ietf.org/html/rfc7372)
* [Validation Tool](https://www.kitterman.com/spf/validate.html) and [Easy DMARC](https://easydmarc.com/tools/spf-record-raw-check-validate)
* Contains: 
  * policy framework
  * authentication method
  * specialized headers 
* Setup: 
  * Add TXT DNS Record with value: 
    * Indicate what version of the policy framework you are using: v=spf1 
    * Specify allowed IP address or domain that resolves to an IP address.  Options are:
      * include:<domain>
      * a
      * mx
      * ip4 
      * ip6
      * redirect
    * Example Values: 
      * Google: v=spf1 include:_spf.google.com ~all
      * Sendgrid: 
        * If no SPF record on your domain: v=spf1 include:sendgrid.net -all
        * If already an SPF record on your domain, add sendgrid to the end before the "all" argument: 
          * Before: v=spf1 a -all
          * After: v=spf1 a include:sendgrid.net -all
          * **Note**: Using "-all" vs "~all" indicates that this SPF record is the only record used to authenticate mail for your domain. 

**DKIM (Domain Keys Identified Mail)**
* Purpose: Ensures the contents of your emails have not been tampered with or comporomised. 
* Works by adding digital signature to header. When email is received, the public key is retrieved from the DNS to verify the signature.
* [Standard](https://tools.ietf.org/html/rfc8301) and [Updated](https://tools.ietf.org/html/rfc7372)
* [Validation Tool](http://dkimvalidator.com/)
* Setup: 
  * Sendgrid (**Note** If Automated Security is checked, then SPF and DKIM records are handled for you): 
    * Go to Settings -> Sender Authentication -> Authenticate your domain: 
      * Choose DNS Host
      * Yes to branding the links for the domain (this gets rid of the "sent via Sendgrid" message)
      * Click Next
      * Enter the domain you send email from
      * Check automated security
      * Click Next
      * Add DNS records

**DMARC (Domain-based Message Authentication, Reporting, and Conformance)**
* Purpose: Tells the receiving email server what to do if SPF and DKIM validation fails.
* Links Sender's domain name with what is listed in the "FROM" header
* [Standard](https://tools.ietf.org/html/rfc7489)
* [Validation Tool](https://powerdmarc.com/power-dmarc-toolbox/)
* Setup: 
  * Ensure that both SPF and DKIM are setup properly using the validation tools first
  * Configuration: 
    * Specify version: v=DMARC1
    * Specify the policy: p=<policy type>.  Types:
      * p=none: no action should be taken.  If a failure occurs then message should still be delivered.  Failure is still logged in reports
      * p=quarantine: Failures should be quarantined.  Usually means that message is sent to spam folder.Failure is still logged in reports
      * p=reject: Failures will be rejected.  Usually means message will be deleted.  This message may be bounced to the envelope from address
    * Specify where to deliver aggregatre reports: rua=<email address to send reports to>
    * Specify where to deliver forensic reports: ruf=<email address to send reports to>
    * Specify what format to put the reports in: rf=<report format>
      * rf=afrf: default.  [Authentication Failure Reporting Format](https://tools.ietf.org/html/rfc6591)
      * rf=iodef
    * Specify what type of failures to report: fo=<type of failure>
      * fo=0: default. send a report if BOTH spf and dkim fail.
      * fo=1: send if either spf OR dkim fail
      * fo=d: send a report only if dkim fails.
      * fo=s: send a report only if spf fails
    * Specify what interval you wish to receive aggregate reports: ri=<time in seconds between report send>
      * default is 86400 which is every 24 hours
    * Specify how strictly to apply spf and dkim values to pass a check. aspf for spf and adkim for dkim
      * values are either r for relaxed or s for strict
        * r: any return-path domain matching the root of the domain set in the spf or dkim record will pass.  Allows for CNAME addresses to pass.
        * s: only return-path domains that match the domain set in SPF or DKIM EXACTLY will pass
      * aspf=r
      * aspf=s
      * adkim=r
      * adkim=s
    * Specify if subdomains should have a different policy: sp=<policy type (defined above)>
    * Specify the percentage of email to which DMARC policy will be applied: pct=<1-100 value>
      * If policy is set to quarantine and pct=50 then half of failing email will be quarantined.  This helps gradually ramp up strictness of policy
  * Sendgrid
    * Same process as above for authenticating domain will add CNAME records to DNS
    * Example: v=DMARC1;p=none;sp=none;pct=100;adkim=r;aspf=r;rua=mailto:jacob@1p.solutions;ruf=mailto:jacob@1p.solutions;ri=86400;fo=1


Questions: 
1) what sendgrid destination ip from their servers (they have public facing IPs)?
2) how to configure TLS to be required and verify port required for that?