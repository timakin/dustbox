class Valuation
  def initialize(casharray, rate)
    @cash_flow = casharray
    @rate = rate
  end

  def present_value
    cash = @cash_flow.inject(0) { |sum, x| sum+x }
    cash/((1 + @rate)**(@cash_flow.size))	
  end

  def future_value
    cash = @cash_flow.inject(0) { |sum, x| sum+x }
    cash*((1+@rate)**(@cash_flow.size))
  end

  def npv
    npv = 0
    @cash_flow.each_with_index do |val, i|
      npv += val.to_f/(1.0+@rate)**i.to_f
    end
    npv
  end

  attr_accessor :cash_flow, :rate
end
