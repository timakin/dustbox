#-*- encoding: utf-8 -*-

class Statistics
  def initialize(asset)
    @asset = asset
    @asset_max = asset.max
    @asset_min = asset.min
  end

  def sum
    @asset.inject(:+).to_f
  end

  def mean
    sum = self.sum.to_f
    sum/@asset.size.to_f
  end

  def median
    (@asset_max+@asset.min)/2.to_f
  end

  def variance
    mean = self.mean.to_f
    numerator = @asset.inject(0) { |acc, x| acc+(x-mean)**2 }
    fraction = @asset.size.to_f
    (numerator.to_f/fraction).to_f		
  end

  def standard_deviation
    variance = self.variance.to_f
    Math.sqrt(variance).to_f
  end

  attr_accessor :asset, :asset_max, :asset_min
end

if __FILE__ == $0
  array = [1,2,3,4,5,6,7,8,9,10]
  test = Statistics.new(array)
  printf "実行結果は以下の通りです\n"
  p test.sum
  p test.mean
  p test.median
  p test.variance
  p test.standard_deviation	
end
