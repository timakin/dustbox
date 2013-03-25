class Triangle
	def initialize(n, a)
		@n = n
		@a = a
	end

	def solve
		ans = 0
		
		0.step(@n-1,1) do |i|
			(i+1).step(@n-1,1) do |j|
				(j+1).step(@n-1,1) do |k|
					leng = @a[i] + @a[j] + @a[k]
					p a[i],a[j],a[k]
					ma = ()
					ma = (@a[i], ((@a[j], @a[k]).max)).max
					print ma
					rest = leng-ma
					print rest
					if ma>rest
						ans = (ans, leng).max
						numbers.max {|a, b| a.to_i <=> b.to_i }
						return ans
					end
				end
			end
		end
	end
end