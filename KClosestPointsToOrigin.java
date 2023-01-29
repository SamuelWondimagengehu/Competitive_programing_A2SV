	public int[][] kClosest(int[][] points, int k) {
		PriorityQueue<int[]> pq = new PriorityQueue<>( (x,y) -> ( (x[0]*x[0] + x[1]*x[1])-
				(y[0]*y[0] + y[1]*y[1])) );
		
		int[][] result = new int[k][2];
		
		for(int[] p : points) {
			pq.offer(p);
		}
		
		for(int i = 0; i < k; i++) {
			result[i] = pq.poll();
		}
		return result;
	}
	
