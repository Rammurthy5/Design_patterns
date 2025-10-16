package main

import "fmt"

// 1. Strategy Interface
type BillingStrategy interface {
	CalculateBill(amount float64) float64
}

// 2. Concrete Strategies (Go structs implementing the interface)
type StandardDiscount struct{}

func (s StandardDiscount) CalculateBill(amount float64) float64 {
	return amount * 0.90
}

type PremiumDiscount struct{}

func (p PremiumDiscount) CalculateBill(amount float64) float64 {
	return amount * 0.80
}

type NoDiscount struct{}

func (n NoDiscount) CalculateBill(amount float64) float64 {
	return amount
}

// 3. Context (Go struct)
type ShoppingCart struct {
	strategy BillingStrategy
	items    []float64
}

// Constructor/Setter
func NewShoppingCart(strategy BillingStrategy) *ShoppingCart {
	return &ShoppingCart{strategy: strategy}
}

func (c *ShoppingCart) SetStrategy(strategy BillingStrategy) {
	c.strategy = strategy
}

func (c *ShoppingCart) AddItem(price float64) {
	c.items = append(c.items, price)
}

func (c *ShoppingCart) Checkout() {
	var totalAmount float64
	for _, price := range c.items {
		totalAmount += price
	}
	finalBill := c.strategy.CalculateBill(totalAmount)
	fmt.Printf("Total items cost: $%.2f\n", totalAmount)
	fmt.Printf("Final bill after discount: $%.2f\n", finalBill)
}

func main() {
	// Client Usage
	cart := NewShoppingCart(StandardDiscount{}) // Starts with Standard Discount
	cart.AddItem(100)
	cart.AddItem(50)
	cart.Checkout()

	fmt.Println("--------------------")

	// Change strategy at runtime
	cart.SetStrategy(PremiumDiscount{})
	cart.AddItem(20)
	cart.Checkout()
}
