<template>
  <div>
    <div class="ui green inverted menu">
      <div class="header item">Food Router</div>
	  <nuxt-link to="/analytics" class="item">Analytics</nuxt-link>
      <div class="right menu">
        <a class="item" href="/"><i class="home icon"></i>Home</a>
        <nuxt-link to="/uploadproduct" class="ui item" style="background-color:red">Give your extra food</nuxt-link>
        <!-- <nuxt-link to="/register" class="ui item">Register / Sign In</nuxt-link> -->
         <nuxt-link to="/register" class="ui item" v-if="!isloggedin">Login / Sign Up</nuxt-link>
        <button class="ui item" v-if="isloggedin" @click.prevent="logout">Logout</button> 
      </div>
    </div>
    <nuxt />
  </div>
</template>

<script>
export default {
	methods:{
		logout(){
			localStorage.clear()
			location.reload()
		}
	},
  computed: {
    isloggedin() {
      if (process.browser)
        return localStorage.uid == undefined ? false : true;
    }
  }
};
</script>