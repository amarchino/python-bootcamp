def func():
    print('FUNC() IN ONE.PY')

print('TOP LEVEL IN ONE.PY')

if __name__ == '__main__':
    # Run the script
    print('ONE.PY is being run directly!')
else:
    print('ONE.PY has been imported! Name: "{}"'.format(__name__))