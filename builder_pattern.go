package main

import "fmt"

// 1. Product Struct (The complex object to be built)
type Config struct {
	Host       string
	Port       int
	TimeoutSec int
	UseTLS     bool
}

// 2. Concrete Builder Struct
type ConfigBuilder struct {
	config Config
}

// Constructor for the Concrete Builder (takes mandatory fields)
func NewConfigBuilder(host string) *ConfigBuilder {
	return &ConfigBuilder{
		config: Config{
			Host:       host,
			Port:       8080, // Set default for optional Port
			TimeoutSec: 30,   // Set default for optional Timeout
			UseTLS:     false,
		},
	}
}

// Builder Step: Set Port (Returns the builder struct for chaining)
func (b *ConfigBuilder) SetPort(port int) *ConfigBuilder {
	b.config.Port = port
	return b
}

// Builder Step: Set Timeout
func (b *ConfigBuilder) SetTimeout(sec int) *ConfigBuilder {
	b.config.TimeoutSec = sec
	return b
}

// Builder Step: Enable TLS
func (b *ConfigBuilder) EnableTLS() *ConfigBuilder {
	b.config.UseTLS = true
	return b
}

// Build Method (Finalizes the product)
func (b *ConfigBuilder) Build() Config {
	// Optional: Validation logic can go here before returning
	if b.config.Host == "" {
		panic("Host is required!")
	}
	return b.config
}

func main() {
	// Building a custom configuration
	customConfig := NewConfigBuilder("api.service.com").
		SetPort(443).
		SetTimeout(60).
		EnableTLS().
		Build()

	fmt.Printf("Custom Config: %+v\n", customConfig)

	// Building a configuration using only defaults
	defaultConfig := NewConfigBuilder("localhost").Build()

	fmt.Printf("Default Config: %+v\n", defaultConfig)
}
