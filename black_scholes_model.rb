class BlackScholesModel
	def initialize(x, S, X, T, r, v)
		@x, @S, @X, @T, @r, @v = x, S, X, T, r, v
	end
	
	def cumulative_normal_distribution
		a1, a2, a3, a4, a5 = 0.31938153, -0.356563782, 1.781477937, -1.821255978, 1.330274429
		l = x.abs
		k = k = 1.0 / (1.0 + 0.2316419 * l)
		w = 1.0 - 1.0 / Math.sqrt(2*Math::PI)*Math.exp(-l*l/2.0) * (a1*k + a2*k*k + a3*(k**3) + a4*(k**4) + a5*(k**5))
		w = 1.0 - w if x < 0
		return w
	end

	def call_option
		cnd = self.cumulative_normal_distribution
		
	end

	def put_option
		cnd = self.cumulative_normal_distribution
	end

end