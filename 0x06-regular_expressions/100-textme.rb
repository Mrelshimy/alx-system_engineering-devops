#!/usr/bin/env ruby
sender = ARGV[0].scan(/\[from:(\w+)\]/)
receiver = ARGV[0].scan(/\[to:(\w+)\]/)
flags = ARGV[0].scan(/\[flags:(.*?)\]/)
puts [sender, receiver, flags].join(',')
