<template>
    <div>
        <h1 style="text-align:center">Food Inspector</h1>
        <div class="ui container">
            <form class="ui form" @submit.prevent="fetchorder">
                <div class="field">
                    <label>Enter Product ID</label>
                    <input type="text" placeholder="Order ID" v-model="orderid">
                </div>
                <button class="ui button" type="submit">Submit</button>
            </form>
            <div v-if="loaded">
                <div class="ui segment">
                    <div class="ui two column grid">
                        <div class="row">
                            <div class="column">
                                <h5>From</h5>
                                <h1>{{product.Customer_Name}}</h1>
                                <h4>{{product.Address1+', '+product.Address1+', '+product.City+', '+product.PinCode}}</h4>
                            </div>
                            <!-- <div class="column" style="text-align:right">
                                <h5>To</h5>
                                <h1>{{order.to.Customer_Name}}</h1>
                                <h4>{{order.tolocation.Address1+', '+order.tolocation.Address1+', '+order.tolocation.City+', '+order.tolocation.PinCode}}</h4>
                            </div> -->
                        </div>
                    </div>
                </div>
                <div class="ui segment">
                    <h4>Product Images</h4>
                    <img v-for="(x,i) in product.images" :key="i" :src="x.Image_Location" alt="" style="width:300px;height:auto">
                    <h5>Cooked: {{product.cooked}}</h5>
                </div>
                <div class="ui segment" v-if="product.Verified=='0'">
                    <h4 style="text-align:center">Do you approve this food to be sold?</h4>
                    <br>
                    <center>
                        <button class="ui icon button green" @click.prevent="orderverify">
                            <i class="check icon"></i>
                        </button>
                        <button class="ui icon button red" @click.prevent="ordernotverify">
                            <i class="close icon"></i>
                        </button>
                    </center>
                </div>
                <div class="ui segment" v-else>
                    <h4>This item has already completed verification process</h4>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            orderid:'',
            order:{},
            loaded:false,
            product:{}
        }
    },
    methods:{
        fetchorder(){
            // this.$axios.get("/getorder/"+this.orderid).then(response=>{
            //     this.order=response.data
            //     this.loaded=true
            // })
            this.$axios.get("/getProducts/"+this.orderid).then(response=>{
                this.product=response.data
                this.loaded=true
            })
        },
        orderverify(){
            this.$axios.get("/orderverify/"+this.product.product_id+"/1").then(response=>{
                location.reload()
            })
        },
        ordernotverify(){
            this.$axios.get("/orderverify/"+this.product.product_id+"/-1").then(response=>{
                location.reload()
            })
        }
    }
}
</script>

<style>
h1,h2,h3,h4,h5,h6{
    margin: 0   
}
</style>