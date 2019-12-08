<template>
    <div>
        <div class="ui container">
            <div class="ui placeholder segment">
                <div class="ui two column very relaxed stackable grid">
                    <div class="column">
                        <h1 style="text-align:center">Sign In</h1>
                        <form class="ui form" @submit.prevent="signin">
                            <div class="field">
                            <label>Username</label>
                            <div class="ui left icon input">
                                <input type="text" placeholder="Username" v-model="login.username">
                                <i class="user icon"></i>
                            </div>
                            </div>
                            <div class="field">
                            <label>Password</label>
                            <div class="ui left icon input">
                                <input type="password" v-model="login.password" placeholder="Password">
                                <i class="lock icon"></i>
                            </div>
                            </div>
                            <button type="submit" class="ui blue submit button">Login</button>
                        </form>
                    </div>
                    <div class="middle aligned column">
                        <h1 style="text-align:center">Register</h1>
                        <form class="ui form" @submit.prevent="register">
                            <div class="field">
                                <label>Username</label>
                                <div class="ui left icon input">
                                    <input type="text" placeholder="Username" v-model="user.username">
                                    <i class="user icon"></i>
                                </div>
                                </div>
                            <div class="field">
                                <label>Password</label>
                                <div class="ui left icon input">
                                    <input type="password" v-model="user.password">
                                    <i class="lock icon"></i>
                                </div>
                            </div>
                            <div class="field">
                                <label>Full Name</label>
                                <div class="ui left icon input">
                                    <input type="text" v-model="user.Customer_Name">
                                    <i class="user icon"></i>
                                </div>
                            </div>
                            <div class="field">
                                <label>Contact</label>
                                <div class="ui left icon input">
                                    <input type="text" v-model="user.Contact_No">
                                    <i class="user icon"></i>
                                </div>
                            </div>
                            <button type="submit" class="ui blue submit button">Register</button>
                        </form>
                    </div>
                </div>
                <div class="ui vertical divider">
                    Or
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            user:{
                username:'',
                password:'',
                Customer_Name: '',
                Contact_No: ''
            },
            login:{
                username:'',
                password:'',
            }
        }
    },
    methods:{
        register(){
            this.$axios.post("/insertcustomer",this.user).then(response=>{
                this.$router.push("/uploadproduct")
            })
        },
        signin(){
            this.$axios.post("/login", this.login).then(response=>{
                if (response.data==null)
                    alert("Invalid credentials!")
                else
                {
                    if(process.browser)
                    localStorage.setItem('uid',response.data.userid)
                    location.href="/"
                }
            })
        }
    }
}
</script>

<style>

</style>