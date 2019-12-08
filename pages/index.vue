<template>
	<div>
		<h1 style="text-align:center">Food Market</h1>
		<div class="ui container">
			<div class="ui">
				<div class="ui four column grid" v-if="loaded">
					<div class="row">
						<div class="column" v-for="(x,i) in products" :key="i">
							<div class="ui card">
								<div class="image">
									<img :src="x.Image_Location">
								</div>
								<div class="content">
									<nuxt-link :to="'/details/'+x.product_id" class="header">{{x.product_name}}</nuxt-link>
									<div class="meta">
									</div>
									<div class="description" v-if="x.Expiry_date!=null">
										Expiry Date: {{x.Exipry_date}}
									</div>
								</div>
								<div class="extra content">
									<a v-if="x.Verified=='0'">
										Not Verified
									</a>
									<a v-else style="color:green">
										<i class="check circle icon"></i>
										Verified
									</a>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	data(){
		return {
			products:[],
			loaded:false
		}
	},
	created(){
		this.getproducts()
	},
	methods:{
		getproducts(){
			this.$axios.get("/getProducts").then(response=>{
				this.products=response.data
				this.loaded=true
			})
		}
	}
}
</script>

<style>

</style>