Odoo Project - Feedback Management Module

This Odoo project provides a feedback management system allowing employees to submit, categorize, and rate feedback about their work environment. The module also includes attachment support, localization for English and Arabic, and user-specific access rights.
Features

    Employee Feedback Submission: Employees can submit feedback with categories, ratings, and attachments.
    Categories: Classify feedback into categories like "Work Environment", "Management", and "Team Dynamics".
    Attachment Support: Upload files (e.g., screenshots, documents) to provide additional context for feedback.
    Feedback Rating System: Employees rate aspects of their work environment (1 to 5 stars), with ratings visible to managers.
    Access Control: Feedback can be created or edited only when its status is "Pending". Deletion is restricted.
    Localization: English and Arabic translations for a multilingual experience.

Installation

    Clone this repository to your Odoo custom modules directory.

git clone https://github.com/your-username/your-repo-name.git

Install dependencies if any (using requirements.txt).

    pip install -r requirements.txt

    Restart the Odoo server and activate the module from the Odoo app list.

Usage

    Navigate to the Feedback module from the Odoo dashboard.
    Submit Feedback:
        Select the category, add a description, choose a rating, and upload any necessary files.
        Save the feedback. It will be marked as "Pending" for review.
    View Feedback:
        Managers can view feedback, attachments, and average ratings for work environment assessments.

Access Rights

    Employees: Can create and edit feedback when its status is "Pending". Cannot delete feedback.
    Managers: Can view all feedback and see average ratings.

Project Structure

    Models: Contains data structure and business logic.
    Views: XML files defining forms, lists, and tree views for the feedback records.
    Security: Includes access rules and model access definitions for role-based permissions.

Localization

    Supported Languages: English, Arabic
    To switch languages, adjust user settings in Odoo.

Contributing

    Fork the repository.
    Create a new feature branch.
    Commit your changes.
    Push to the branch.
    Submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Contact
