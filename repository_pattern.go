package main

import (
	"fmt"
	"sync"
)

// 1. Domain Model (The object the application uses)
type Product struct {
	ID    int
	Name  string
	Price float64
}

// 2. Repository Interface (Defines the contract for data access)
type ProductRepository interface {
	Save(product Product) error
	FindByID(id int) (Product, error)
	Update(product Product) error
}

// 3. Concrete Repository (Implementation using an in-memory map)
type InMemoryProductRepository struct {
	data   map[int]Product
	nextID int
	mutex  sync.Mutex
}

// Constructor for the concrete repository
func NewInMemoryProductRepository() *InMemoryProductRepository {
	return &InMemoryProductRepository{
		data:   make(map[int]Product),
		nextID: 1,
	}
}

// Concrete implementation of Save
func (r *InMemoryProductRepository) Save(product Product) error {
	r.mutex.Lock()
	defer r.mutex.Unlock()

	if product.ID == 0 {
		product.ID = r.nextID
		r.nextID++
	}
	r.data[product.ID] = product
	fmt.Printf("InMemory: Saved product %s with ID %d\n", product.Name, product.ID)
	return nil
}

// Concrete implementation of FindByID
func (r *InMemoryProductRepository) FindByID(id int) (Product, error) {
	r.mutex.Lock()
	defer r.mutex.Unlock()

	if product, found := r.data[id]; found {
		return product, nil
	}
	return Product{}, fmt.Errorf("product not found with ID: %d", id)
}

// Concrete implementation of Update
func (r *InMemoryProductRepository) Update(product Product) error {
	r.mutex.Lock()
	defer r.mutex.Unlock()

	if _, found := r.data[product.ID]; found {
		r.data[product.ID] = product
		fmt.Printf("InMemory: Updated product ID %d\n", product.ID)
		return nil
	}
	return fmt.Errorf("cannot update: product ID %d not found", product.ID)
}

func main() {
	// The variable uses the interface type
	var repo ProductRepository = NewInMemoryProductRepository()

	// Create a new product
	laptop := Product{Name: "Laptop", Price: 1200.00}
	repo.Save(laptop) // ID will be assigned internally

	// Find the product (assume ID is 1 from the internal counter)
	laptop_id := 1
	found_product, err := repo.FindByID(laptop_id)
	if err == nil {
		fmt.Printf("Found: %+v\n", found_product)
	}

	// Update the product
	found_product.Price = 1150.00
	repo.Update(found_product)

	// Verify update
	updated_product, _ := repo.FindByID(laptop_id)
	fmt.Printf("Updated Price: %.2f\n", updated_product.Price)
}
