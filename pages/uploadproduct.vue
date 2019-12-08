<template>
    <div>
        <div class="ui container">
            <div class="ui segment">
                <div class="ui form">
                    <h1>Enter your food details</h1>
                    <div class="ui two column grid">
                        <div class="row">
                            <div class="column" v-if="!showupload">
                                <form class="ui form" @submit.prevent="insertproduct">
                                    <div class="field">
                                        <label>Title</label>
                                        <input type="text" placeholder="Title" v-model="product.product_name">
                                    </div>
                                    <div class="field">
                                        <label>Address</label>
                                        <select v-model="product.selectedlocation">
                                            <option :value="x.Location_id" v-for="(x,i) in locations" :key="i">{{x.Address1+', '+x.Address2+', '+x.City+', '+x.State+', '+x.PinCode}}</option>
                                        </select>
                                    </div>
                                    <div class="inline field">
                                            <input type="checkbox" tabindex="0" v-model="product.cooked">
                                            <label>Cooked Food</label>
                                    </div>
                                    <div class="inline field">
                                            <input type="checkbox" tabindex="0" v-model="product.perishable">
                                            <label>Perishable</label>
                                    </div>
                                    <div class="field">
                                        <div class="ui checkbox">
                                            <input type="checkbox" tabindex="0" class="hidden">
                                            <label>I agree that all food items are undamaged according to my knowledge and contains no harmful ingredient which may affect consumers' health.</label>
                                        </div>
                                    </div>
                                    <button class="ui button" type="submit">Submit</button>
                                </form>
                            </div>
                            <div class="column" v-else>
                                <label for="">Upload images</label>
                                <div v-if="complete">
                                    <div class="ui icon message">
                                        <i class="check icon"></i>
                                        <div class="content">
                                            <div class="header">
                                            Your product is uploaded successfully
                                            </div>
                                            <p>Food Inspector <b>{{inspector.name}}</b> is assigned to verify your product and will be arriving to your location shortly.</b></p>
                                            <nuxt-link to="/inspector" class="ui button primary">Food Inspector</nuxt-link>
                                        </div>
                                    </div>
                                </div>
                                <file-pond
                                    name="test"
                                    ref="test"
                                    label-idle="Drop files here..."
                                    allow-multiple="false"
                                    :server="'http://10.1.3.206:5000/uploadimage/'+productid"
                                    accepted-file-types="image/jpeg, image/png"
                                    v-bind:files="myFiles"
                                    v-on:processfile="addtopreview"
                                    @processfiles="handleComplete"
                                    />

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import vueFilePond from 'vue-filepond';
import 'filepond/dist/filepond.min.css';
import 'filepond-plugin-image-preview/dist/filepond-plugin-image-preview.min.css';
import FilePondPluginFileValidateType from 'filepond-plugin-file-validate-type';
import FilePondPluginImagePreview from 'filepond-plugin-image-preview';
const FilePond = vueFilePond( FilePondPluginFileValidateType, FilePondPluginImagePreview );
export default {
    data(){
        return {
            myFiles: [],
			uploadedfile:'',
			detectedtext:'',
            loading: false,
            product:{
                product_name: '',
                cooked: false,
                perishable: false,
                customer_id: localStorage.getItem('uid'),
                selectedlocation:1
            },
            showupload: false,
            productid:'',
            locations:[],
            complete: false,
            inspector:{}
        }
    },
    components: {
        FilePond
    },
    created(){
        this.getlocations()
        if(process.browser)
        $('.ui.checkbox').checkbox();
    },
    methods: {
		addtopreview(error, file){
			// alert("done")
		},
        insertproduct(){
            this.$axios.post("/insertproduct", this.product).then(response=>{
                this.showupload=true
                this.productid=response.data
            })
        },
        getlocations(){
            this.$axios.get("/getlocations").then(response=>{
                this.locations=response.data
            })
        },
        handleComplete(){
            this.$axios.put("/assignFoodInspector/"+this.productid).then(response=>{
                this.inspector=response.data
                this.complete=true
            })
        }
    },
}
</script>

<style>

</style>