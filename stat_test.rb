#-*- encoding: utf-8 -*-

require "test/unit"

require_relative "statistics"

class StatisticsTest < Test::Unit::TestCase
	def test1
		array = [2,3,4,4,5,56,6,78,3]
		test = Statistics.new(array)
		printf "実行結果は以下の通りです\n"
		p test.sum
		p test.mean
		p test.median
		p test.variance
		p test.standard_deviation
		p ""
	end	
	def test2
		array = [1.23,2345,2456,2,34,5,6,7,8,5.345]
		test = Statistics.new(array)
		printf "実行結果は以下の通りです\n"
		p test.sum
		p test.mean
		p test.median
		p test.variance
		p test.standard_deviation		
	end
end


