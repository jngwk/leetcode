# @param {String} s
# @return {Integer}
def score_of_string(s)
  s.chars.each_cons(2).sum { |a, b| (a.ord - b.ord).abs }
end
