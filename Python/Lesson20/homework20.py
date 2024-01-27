import re

data = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78'

pattern = r'\+*\d{1}\s*\(*\s*\d{3}\s*\)*\s*\d{3}[\s-]*\d{2}[\s-]*\d{2}'

print(re.findall(pattern, data))
