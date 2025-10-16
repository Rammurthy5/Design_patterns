package main

import "fmt"

// 1. State Interface (Go interface)
type DocumentState interface {
	RequestReview(doc *Document)
	Publish(doc *Document)
	GetName() string
}

// 2. Concrete States
type Draft struct{}

func (d Draft) RequestReview(doc *Document) {
	fmt.Println("Draft: Sending document to moderation.")
	doc.setState(Moderation{})
}
func (d Draft) Publish(doc *Document) {
	fmt.Println("Draft: Cannot publish directly from Draft. Needs review first.")
}
func (d Draft) GetName() string { return "Draft" }

type Moderation struct{}

func (m Moderation) RequestReview(doc *Document) {
	fmt.Println("Moderation: Document is already under review.")
}
func (m Moderation) Publish(doc *Document) {
	fmt.Println("Moderation: Document approved and published.")
	doc.setState(Published{})
}
func (m Moderation) GetName() string { return "Moderation" }

type Published struct{}

func (p Published) RequestReview(doc *Document) {
	fmt.Println("Published: Cannot request review on a Published document.")
}
func (p Published) Publish(doc *Document) {
	fmt.Println("Published: Document is already live.")
}
func (p Published) GetName() string { return "Published" }

// 3. Context
type Document struct {
	currentState DocumentState
	Content      string
}

func NewDocument(content string) *Document {
	// Start in the initial state (Draft)
	return &Document{
		Content:      content,
		currentState: Draft{},
	}
}

func (doc *Document) setState(newState DocumentState) {
	fmt.Printf("Document: Changing state from %s to %s\n", doc.currentState.GetName(), newState.GetName())
	doc.currentState = newState
}

// Delegate actions to the current state
func (doc *Document) RequestReview() {
	doc.currentState.RequestReview(doc)
}

func (doc *Document) Publish() {
	doc.currentState.Publish(doc)
}

func main() {
	doc := NewDocument("My new article content.")
	fmt.Printf("Initial State: %s\n", doc.currentState.GetName())
	fmt.Println("--------------------")

	// Attempt to publish from Draft (will fail/be blocked)
	doc.Publish()

	// Request review (Draft -> Moderation)
	doc.RequestReview()
	fmt.Println("--------------------")

	// Attempt to publish from Moderation (will succeed)
	doc.Publish()
	fmt.Println("--------------------")

	// Attempt to review a published document (will fail/be blocked)
	doc.RequestReview()
}
