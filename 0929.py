class Solution:
  def numUniqueEmails(self, emails: list[str]) -> int:
    a = set()
    for email in emails:
      name, domain = email.split('@')
      local = name.split('+')[0].replace('.', '')
      a.add(local + '@' + domain)
    return len(a)
      
a = Solution()
arr = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
s = a.numUniqueEmails(arr)
print(s)