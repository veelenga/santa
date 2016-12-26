require 'json'
require 'net/http'

URL = 'https://cdn.rawgit.com/veelenga/santa/master/happy_new_year.json'

language = ARGV[0]
codes = JSON.parse(Net::HTTP.get URI(URL))
puts codes[language] || codes['eng']
