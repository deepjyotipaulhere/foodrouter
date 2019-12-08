<template>
    <div>
        <div class="ui container">
            <div class="ui segment" v-if="loaded">
                <div class="ui grid two column">
                    <div class="row">
                        <div class="column">
                            <img :src="product.images[0].Image_Location" alt="">
                        </div>
                        <div class="column">
                            <h1>{{product.product_name}}</h1>
                            <h4 style="color:#777">Expiry Date: {{product.Exipry_date}}</h4>
                            <h5 style="color:green" v-if="product.Verified!='0'">
                                <i class="check circle icon"></i>
                                Verified
                            </h5>
                            <h5 style="color:#777">
                                Not Verified
                            </h5>
                            <div class="field">
                                <label>Deliver to</label>
                                <select v-model="selectedlocation">
                                    <option :value="x.Location_id" v-for="(x,i) in locations" :key="i">{{x.Address1+', '+x.Address2+', '+x.City+', '+x.State+', '+x.PinCode}}</option>
                                </select>
                            </div>
                            <br>
                            <button class="ui primary button" @click.prevent="insertorder">Order</button>
                        </div>
                    </div>
                </div>
            </div>
            <br>
            <br>
            <div class="ui icon message" v-if="uploaded">
                <i class="check icon"></i>
                <div class="content">
                    <div class="header">
                    Your order is placed. Order ID: {{orderid}}
                    </div>
                    <p>A delivery executive will be assigned shortly to deliver to your location</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            product:{},
            loaded: false,
            locations:[],
            selectedlocation:1,
            uploaded: false,
            orderid:''
        }
    },
    created(){
        this.getproductdetails()
        this.getlocations()
    },
    methods:{
        getlocations(){
            this.$axios.get("/getlocations").then(response=>{
                this.locations=response.data
            })
        },
        getproductdetails(){
            this.$axios.get("/getProducts/"+this.$route.params.id).then(response=>{
                this.product=response.data
                this.loaded=true
            })
        },
        insertorder(){
            this.$axios.post("/insertorder", {
                to: localStorage.getItem('uid'),
                productid: this.$route.params.id,
                tolocation: this.selectedlocation
            }).then(response=>{
                this.uploaded=true
                this.orderid=response.data
            })
        }
    }
}
</script>

<style>

</style>