app.component('product-display', {
  props: {
    premium: {
      type: Boolean,
      required: true
    }
  },
  template:
  /*html*/
  `
  <div class="product-display">
  <div class="product-container">
    <div class="product-image">
      <img v-bind:src="image" v-bind:class="{ 'out-of-stock-img': !inStock }">
    </div>
    <div class="product-info">
      <h1>{{ title }}</h1>
      <!-- <p v-show="inStock">In Stock</p> -->
      <!-- <p v-if="inventory > 10">In Stock</p>
      <p v-else-if="inventory <= 10 && inventory > 0">Almost sold out!</p>
      <p v-else>Out of Stock</p> -->
      <p v-if="inStock">In Stock</p>
      <p v-else>Out of Stock</p>

      <p>Shipping: {{ shipping }}</p>

      <p v-if="onSale">{{ saleMessage }}</p>
      <p v-else>notSale</p>
      <ul>
        <li v-for="detail in details">{{ detail }}</li>
      </ul>
      <div 
        v-for="(variant, index) in variants" 
        :key="variant.id" 
        v-on:mouseover="updateVariant(index)"
        class="color-circle"
        v-bind:style="{ backgroundColor: variant.color }"
        >
      </div>
      <!-- backgroundColor -> background-color -->

      <div v-for="(size, index) in sizes" :key="index">{{ size }}</div>
      <button 
        class="button"
        :class="{ disabledButton: !inStock }"
        :disabled="!inStock" 
        v-on:click="addToCart"
        >Add to Cart</button>
      <button 
        class="button" 
        v-on:click="deleteFromCart">
        Delete from Cart</button>
    </div>
  </div>
</div>
`,
  data() {
    // data: function() {
    return {
      product: 'Socks',
      brand: 'Vue Mastery',
      selectedVariant: 0,
      //image: './assets/images/socks_green.jpg',
      // inStock: false,
      inventory: 10,
      onSale: true,
      details: ['50% cotton', '30% wool', '20% polyester'],   
      variants: [
        { id: 2234, color: 'green', image: './assets/images/socks_green.jpg', quantity: 50},
        { id: 2235, color: 'blue', image: './assets/images/socks_blue.jpg', quantity: 0},
      ],
      sizes: ['S', 'M', 'L', 'XL'],
    }
  },

  methods: {
    addToCart() {
      this.$emit('add-to-cart', this.variants[this.selectedVariant].id)
    },
    deleteFromCart() {
      this.$emit('delete-from-cart', this.variants[this.selectedVariant].id)
    },
    updateImage(variantImage) {
      this.image = variantImage
    },
    updateVariant(index) {
      this.selectedVariant = index
    },
  },

  computed: {
    title() {
      return this.brand + ' ' + this.product
    },
    image() {
      return this.variants[this.selectedVariant].image
    },
    inStock() {
      return this.variants[this.selectedVariant].quantity
    }, // data property => computer property
    saleMessage() {
      if (this.onSale) {
        return this.brand + this.product + 'is on sale.'
      }
      return ''
    },
    shipping() {
      if (this.premium) {
        return 'Free'
      }
      return 2.99
    }
  }
})