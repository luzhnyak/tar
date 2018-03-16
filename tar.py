import tarfile
import sys

# if len(sys.argv) == 1:
#     print("usage: %s <tar archive>" % (sys.argv[0]))
#     sys.exit(0)

# arhive_name = sys.argv[1]

#archive_encoding = 'cp1251'
archive_encoding = 'utf-8'

tar = tarfile.open(name="domain_data.tar", mode='r', bufsize=16*1024, encoding=archive_encoding)
tar.extractall()
tar.close()