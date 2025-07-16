# Bad Word Lists for Message Filtering

## Purpose of This Folder

This folder contains comprehensive lists of offensive, derogatory, and inappropriate words/phrases across multiple languages. These lists are used **exclusively** for automated content filtering in our Discord status update application.

## How We Use These Lists

1. **Content Filtering**: The Python script references these lists to prevent any offensive language from appearing in Discord status updates
2. **Safety Measure**: Acts as a safeguard against accidental transmission of inappropriate content via speech recognition
3. **Multilingual Support**: Covers various languages to accommodate diverse user bases

## Important Legal and Ethical Considerations

### GitHub Compliance
- This content is **permitted** under GitHub's Acceptable Use Policies as:
  - It's used for research/filtering purposes
  - Not promoting or encouraging harmful content
  - Necessary for developing effective content moderation tools
- These lists are **not**:
  - Distributed as standalone content
  - Used to harass or target individuals/groups
  - Shared outside their intended filtering context

### Our Stance
We **categorically reject** and **do not endorse** any of the terms contained in these lists. Their inclusion serves strictly for:
- Identification purposes in automated filtering systems
- Prevention of harmful language propagation
- Development of protective measures against online abuse

## Implementation Details

The filtering system works as follows:
1. Speech recognition converts voice to text
2. Text is compared against these lists
3. Any matches trigger:
   - Word masking (****)

## Maintenance Guidelines

1. **Updates**: Lists should be periodically reviewed and updated
2. **Additions**: New entries must be:
   - Verifiably offensive/dangerous
   - Contextually relevant for filtering
3. **Removals**: Terms that become outdated or change meaning should be removed

## Warning

Misuse of these lists for purposes other than content filtering violates:
- Project guidelines
- GitHub's Terms of Service
- Potentially applicable laws

Use only as intended in the specified filtering context.
