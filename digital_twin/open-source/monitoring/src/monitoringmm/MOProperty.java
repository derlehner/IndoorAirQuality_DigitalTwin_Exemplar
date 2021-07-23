/**
 */
package monitoringmm;

import org.eclipse.emf.ecore.EClass;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>MO Property</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link monitoringmm.MOProperty#getEclass <em>Eclass</em>}</li>
 * </ul>
 *
 * @see monitoringmm.MonitoringmmPackage#getMOProperty()
 * @model
 * @generated
 */
public interface MOProperty extends MOElement {
	/**
	 * Returns the value of the '<em><b>Eclass</b></em>' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Eclass</em>' reference.
	 * @see #setEclass(EClass)
	 * @see monitoringmm.MonitoringmmPackage#getMOProperty_Eclass()
	 * @model
	 * @generated
	 */
	EClass getEclass();

	/**
	 * Sets the value of the '{@link monitoringmm.MOProperty#getEclass <em>Eclass</em>}' reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Eclass</em>' reference.
	 * @see #getEclass()
	 * @generated
	 */
	void setEclass(EClass value);

} // MOProperty
