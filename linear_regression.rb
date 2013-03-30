#-*- encoding: utf-8 -*-

require_relative "statistics"

class LinearRegression
	def initialize(xn, yn)
		@xn, @yn = xn, yn
		p "XとYの個数が一致しません" if @xn.length != @yn.length
	end
	
	def slope #傾き
		x_mean, y_mean = mean(@xn), mean(@yn)

		numerator = (0...@xn.length).reduce(0) do |sum, i| #初期値が0で、加えていく考え方。
			sum + ((@xn[i]-x_mean)*(@yn[i]-y_mean))
		end

		denominator = (0...@xn.length).reduce(0) do |sum, i|
			sum + ((@xn[i]-x_mean)**2)
		end

		numerator/denominator
	end

	def intercept #切片
		mean(@yn) -(slope * mean(@xn))
	end

	def mean(x)
		stat = Statistics.new(x)
		stat.mean
	end

	attr_accessor :xn, :yn
end

if __FILE__ == $0
	data_file = File.open("sample-video-view-data.csv")
	data_file.readline # strip off the header
 
	xs, ys = [], []
 
	data_file.each do |line|
  	x, y = line.split(",")
  	xs << Float(x)
  	ys << Float(y)
	end
 
	linear_model = LinearRegression.new(xs, ys)
	puts "Slope: #{linear_model.slope}"
	puts "Intercept: #{linear_model.intercept}"
	puts "\n"
	puts "Estimated Linear Model:"
	puts "Y = #{linear_model.intercept} + (#{linear_model.slope} * X)"
end